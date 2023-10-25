document.getElementById("uploadButton").addEventListener("click", async () => {
    const imageInput = document.getElementById("imageInput");
    const imageFile = imageInput.files[0];
    if (imageFile) {
        const formData = new FormData();
        formData.append("image", imageFile);

        const response = await fetch("/upload/", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();
            const predictionText = document.getElementById("predictionText");
            predictionText.innerText = `Hasil Prediksi: ${data.prediction}`;

            const uploadedImage = document.getElementById("uploadedImage");
            uploadedImage.src = data.image_filename;
            uploadedImage.style.display = "block";
        }
    }
});