const shapesContainer = document.querySelector('#shapes');

async function loadShapes() {
    const response = await fetch('/api/shapes/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    });

    const shapes = await response.json();
    
    shapesContainer.innerHTML = '';
    shapes.forEach(shape => {
        shapesContainer.innerHTML += 
            '<div class="shape flex-column-center-center">' + 
                '<img src="' + shape.image + '" alt="">' +
                '<div class="bar-bg">' + 
                    '<div class="bar"></div>' + 
                    '<span class="bar-text"> 0% voted</span>' + 
                '</div>' + 
            '</div>';
    })
}

loadShapes();