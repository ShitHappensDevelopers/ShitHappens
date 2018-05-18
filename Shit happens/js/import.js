
// script for displaing imported documents in places where these imports was

var importOccured = false;

do {
	importOccured = false;
	var parts = document.querySelectorAll("link[rel=import]");
	Array.prototype.forEach.call(parts, function(element) {
		element.parentElement.insertBefore(element.import.firstChild, element);
		importOccured = true;
	});
} while (importOccured);