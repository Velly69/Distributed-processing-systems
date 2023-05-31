//
//  CarouselView.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 31.05.2023.
//

import SwiftUI

struct CarouselView: View {
    @Binding var selectedImageStyle: ImageStyle
    
    var body: some View {
        GeometryReader { reader in
            ScrollView(.horizontal, showsIndicators: false) {
                HStack {
                    ForEach(ImageStyle.allCases, id: \.self) { imageStyle in
                        Button {
                            selectedImageStyle = imageStyle
                        } label: {
                            ZStack {
                                Image(imageStyle.rawValue)
                                    .resizable()
                                    .background(Color.blue)
                                    .scaledToFill()
                                    .frame(width: reader.size.width * 0.4, height: reader.size.height * 0.5 * 1.4)
                                    .overlay {
                                        RoundedRectangle(cornerRadius: 20)
                                            .stroke(Color.yellow, lineWidth: imageStyle == selectedImageStyle ? 3 : 0)
                                    }
                                    .clipShape(RoundedRectangle(cornerRadius: 20.0))
                                
                                Text(imageStyle.title)
                                    .font(.title3)
                                    .fontWeight(.medium)
                                    .foregroundColor(.white)
                                    .padding(10)
                                    .background(Color.black.opacity(0.8))
                                    .clipShape(RoundedRectangle(cornerRadius: 15))
                                    .padding(.top, 120)
                            }
                        }
                    }
                }
            }
        }
    }
}
