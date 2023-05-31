//
//  PromptView.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 30.05.2023.
//

import SwiftUI

struct PromptView: View {
    @State private var selectedImageStyle = ImageStyle.allCases[0]
    @State private var promptText = ""
    
    var body: some View {
        NavigationView {
            VStack(alignment: .leading) {
                
                TitleView()
                
                CarouselView(
                    selectedImageStyle: self.$selectedImageStyle
                )
                
                Spacer()
                
                Text("Enter a prompt")
                    .font(.title3)
                    .fontWeight(.bold)
                    .foregroundColor(.white)
                
                TextEditor(text: $promptText)
                    .scrollContentBackground(.hidden)
                    .padding()
                    .background(Color.gray.opacity(0.2))
                    .cornerRadius(12.0)
                    .foregroundColor(.white)
                    .tint(.yellow)
                
                VStack(alignment: .center) {
                    NavigationLink {
                        GeneratorView(viewModel: .init(
                            prompt: promptText,
                            imageSelectedStyle: selectedImageStyle
                        ))
                    } label: {
                        Text("Generate")
                            .foregroundColor(.black)
                            .padding()
                            .background(.yellow)
                            .clipShape(Capsule())
                        
                    }
                }
                .frame(maxWidth: .infinity)
            }
            .padding()
            .background(Color.black.edgesIgnoringSafeArea(.all))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        PromptView()
    }
}
