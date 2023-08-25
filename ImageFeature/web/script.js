function handleClick(element){
    let end_point_url = "http://localhost/api/gethog"
    var base64String = "";
    let file = element.files[0];
    let reader = new FileReader();
    reader.onload = () => {
        base64String = reader.result;
        fetch(end_point_url, {
            method: "POST",
            body: JSON.stringify({img: base64String}),
            headers:{"Content-type": "application/json; charset=UTF-8"}
        }
        )
        
        .then((response) => response.json())
        .then((json) => console.log(json));
    };
    reader.readAsDataURL(file);
    }