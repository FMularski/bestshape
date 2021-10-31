// const shapes = document.querySelectorAll('div.shape img');
const dark = document.querySelector('#dark');
const votingPanel = document.querySelector('#voting');
// const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;


function vote(shapeId) {
    dark.classList.add('active');
    votingPanel.classList.add('active');

    fetch('/api/vote/' + shapeId + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        }
    })
    .then(response => {{
        dark.classList.remove('active');
        votingPanel.classList.remove('active');
        
        // update all bars
        const shapesImgs = document.querySelectorAll('div.shape img');

        shapesImgs.forEach(shape => {
            updateBar(shape.getAttribute('shape-id'));
        });

    }})


}
