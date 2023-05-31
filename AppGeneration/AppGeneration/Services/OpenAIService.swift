//
//  OpenAIService.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 30.05.2023.
//

import Foundation
import Alamofire

final class OpenAIService {
    private let endpointURL = "https://api.openai.com/v1/images/generations"
    
    func generateImage(
        promt: String
    ) async throws  -> OpenAIImageResponse{
        let body = OpenAIImageRequestBody(prompt: promt, size: "512x512")
        let headers: HTTPHeaders = [
            "Authorization": "Bearer \(Constants.openAIApiKey)"
        ]
        return try await AF.request(
            endpointURL,
            method: .post,
            parameters: body,
            encoder: .json,
            headers: headers
        ).serializingDecodable(OpenAIImageResponse.self).value
    }
}

struct OpenAIImageResponse: Codable {
    let data: [OpenAIImageURL]
}

struct OpenAIImageURL: Codable {
    let url: String
}

struct OpenAIImageRequestBody: Codable {
    let prompt: String
    let size: String
}
