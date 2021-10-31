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
                '<img src="' + shape.image + '" shape-id="' + shape.id + '">' +
                '<div class="bar-bg">' + 
                    '<div id="bar-' + shape.id + '" class="bar"></div>' + 
                    '<span class="bar-text"> 0% voted</span>' + 
                '</div>' + 
            '</div>';
    })

    const shapesImgs = document.querySelectorAll('div.shape img');

    shapesImgs.forEach(shape => {
        shape.addEventListener('click', () => {
            vote(shape.getAttribute('shape-id'));
        });

        updateBar(shape.getAttribute('shape-id'));
    })
}

loadShapes();