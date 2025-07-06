import os
import re

# Folder containing your HTML files
FOLDER = "."  # current folder

# Lightbox HTML and JS to insert
LIGHTBOX_BLOCK = '''
<div class="lightbox" id="lightbox">
    <img src="" alt="Zoomed Image">
</div>

<script>
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = lightbox.querySelector('img');
    const images = document.querySelectorAll('.ai-images-container img');

    images.forEach(img => {
        img.addEventListener('click', () => {
            lightboxImg.src = img.src;
            lightbox.style.display = 'flex';
        });
    });

    lightbox.addEventListener('click', () => {
        lightbox.style.display = 'none';
        lightboxImg.src = "";
    });
</script>
'''

# Go through all drawingXXXX.html files
for filename in os.listdir(FOLDER):
    if re.match(r"drawing\d{4}\.html", filename):
        path = os.path.join(FOLDER, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Avoid inserting twice
        if '<div class="lightbox" id="lightbox">' in content:
            print(f"Skipped (already contains lightbox): {filename}")
            continue

        # Insert before </body>
        updated_content = content.replace("</body>", LIGHTBOX_BLOCK + "\n</body>")

        with open(path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print(f"Updated: {filename}")
