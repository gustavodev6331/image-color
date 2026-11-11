
document.querySelectorAll(".color-hex").forEach(button => {

    button.addEventListener("click", async () => {

        const hexColor = button.dataset.hex;

        try {
            await navigator.clipboard.writeText(hexColor);

            const originalText = button.textContent;

            button.textContent = "Copied!";

            setTimeout(() => {
                button.textContent = originalText;
            }, 1200);

        } catch (error) {
            console.error("Failed to copy color:", error);
        }

    });

});
