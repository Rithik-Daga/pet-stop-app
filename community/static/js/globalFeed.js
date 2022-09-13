btns = document.getElementsByClassName("update-btn");

btns.array.forEach((element) => {
	element.onclick = () => {
		if (element.style.background_color == "#14191e") {
			element.style.background_color = "var(--hover-color)";
		}
	};
});
