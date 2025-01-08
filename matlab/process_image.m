function processed_image = process_image(image_path)
    % Load the image
    img = imread(image_path);
    
    % Example image processing: Convert to grayscale
    processed_image = rgb2gray(img);
    
    % Save the processed image (optional)
    imwrite(processed_image, 'processed_image.png');
end
