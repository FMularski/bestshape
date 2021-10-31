const bars = document.querySelectorAll('.bar');

function updateBar(shapeId) {
    fetch('/api/vote-ratio/' + shapeId + '/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(ratio => {
        const bar = document.querySelector("#bar-" + shapeId);
        const ratioDisplay = document.querySelector('#bar-' + shapeId + '+span');
        bar.style.width = ratio + '%';
        ratioDisplay.innerText = ratio + '% votes';
    })
}