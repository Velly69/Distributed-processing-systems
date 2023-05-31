//
//  GeneratorViewModel.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 30.05.2023.
//

import Foundation

final class ViewModel: ObservableObject {
    @Published var duration = 0
    @Published var image: URL?
    
    private let prompt: String
    private let imageSelectedStyle: ImageStyle
    
    private let openAIService = OpenAIService()
    
    init(
        prompt: String,
        imageSelectedStyle: ImageStyle
    ) {
        self.prompt = prompt
        self.imageSelectedStyle = imageSelectedStyle
    }
    
    func generateImage() {
        let formattedPrompt = "\(imageSelectedStyle.title) image of \(prompt)"
        
        Task {
            do {
                let generatedImage = try await openAIService.generateImage(promt: formattedPrompt)
                guard let imageURLString = generatedImage.data.first?.url,
                      let imageURL = URL(string: imageURLString) else { return }
                await MainActor.run {
                    self.image = imageURL
                }
            } catch {
                
            }
        }
    }
}

