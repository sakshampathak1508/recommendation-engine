import cv2
import skimage.metrics as metrics

# Function to compare two images using SSIM
def compare_images(image1_path, image2_path):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    
    # Convert the images to grayscale
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Calculate the SSIM score
    ssim_score = metrics.structural_similarity(image1_gray, image2_gray)
    
    return ssim_score

# Example usage
image1_path = 'path_to_image1'
image2_path = 'path_to_image2'
similarity_score = compare_images(image1_path, image2_path)
print(f"Similarity score: {similarity_score}")
