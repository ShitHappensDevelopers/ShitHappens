
// this code helps to toggle window for setting story lifetime
$('#myStoryLife').change(function() {
	$('#mySetStoryLife').toggle(300);
}); 


// for textarea to resize automatically
$('#myWriteStoryTxtAr').on("input", function() {
	var textArea = $('#myWriteStoryTxtAr');
	this.style.height = 0;
	this.style.height = this.scrollHeight + 'px';
	// this.style.height = this.scrollHeight + (textArea.outerHeight() - textArea.height()) / 2 + 'px';
});
