function search () {
    if(e.keyCode === 13){
        e.preventDefault();

        var query = document.getElementById("searchBox").value;

        query = query.replace(" ", "+");
    }
}
