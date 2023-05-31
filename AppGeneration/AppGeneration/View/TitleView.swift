//
//  TitleView.swift
//  AppGeneration
//
//  Created by Alexandr Totskiy on 31.05.2023.
//

import SwiftUI

struct TitleView: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("Generate")
                .font(.title)
                .fontWeight(.bold)
                .foregroundColor(.white)
            
            Text("Choose a style")
                .font(.title3)
                .fontWeight(.bold)
                .foregroundColor(.white)
        }
    }
}
