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
                    '<div class="bar" style="width: ' + shape.votes + '%"></div>' + 
                    '<span class="bar-text">' + shape.votes + '% voted</span>' + 
                '</div>' + 
            '</div>';
    })
}

loadShapes();