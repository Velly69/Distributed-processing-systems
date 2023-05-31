//
//  ImageStyle.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 30.05.2023.
//

import Foundation

enum ImageStyle: String, CaseIterable {
    case empty
    case surrealism
    case realism
    case threeDRender
    case minimalism
    case abstract
    case geometric
    
    var title: String {
        switch self {
        case .empty:
            return "Empty"
        case .surrealism:
            return "Surrealism"
        case .realism:
            return "Realism"
        case .threeDRender:
            return "3D Render"
        case .minimalism:
            return "Minimalism"
        case .abstract:
            return "Abstract"
        case .geometric:
            return "Geometric"
        }
    }
}
