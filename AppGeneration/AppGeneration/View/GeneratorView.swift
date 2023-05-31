//
//  GeneratorView.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 30.05.2023.
//

import SwiftUI

struct GeneratorView: View {
    @ObservedObject var viewModel: ViewModel
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("Generated Image")
                .font(.largeTitle)
                .fontWeight(.bold)
                .foregroundColor(.white)
            VStack {
                AsyncImage(
                    url: viewModel.image
                ) { image in
                    image
                        .resizable()
                        .aspectRatio(1, contentMode: .fit)
                } placeholder: {
                    ProgressView()
                        .frame(width: 100, height: 100)
                }
                .background(Color.gray.opacity(0.2))
                .aspectRatio(contentMode: .fit)
                .frame(maxWidth: .infinity)
                .cornerRadius(20)
                .clipped()
            }
            Spacer()
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(Color.black.edgesIgnoringSafeArea(.all))
        .onAppear {
            viewModel.generateImage()
        }
    }
}

struct GenratorView_Previews: PreviewProvider {
    static var previews: some View {
        GeneratorView(viewModel: .init(
            prompt: "Red car",
            imageSelectedStyle: .realism
        ))
    }
}
