function onClickedEstimateSpecies(){
    var sl = $("#sl")[0]['value']
    var sw = $("#sw")[0]['value']
    var pl = $("#pl")[0]['value']
    var pw = $("#pw")[0]['value']
    var url = "http://127.0.0.1:5000/get_species"
    var myDiv = document.getElementById("species_estimated")

    $.post(url, {
        sepal_length: sl,
        sepal_width: sw,
        petal_length: pl, 
        petal_width: pw
    }, function(data, status){
            console.log(data.species)
            console.log(status)
            myDiv.innerHTML = "<h2>"+ data.species + "</h2>"
    })
}

