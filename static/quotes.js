let nextButton = document.querySelector('.next')
let containerDiv = document.querySelector('.container')
let author = document.querySelector('h4')
let quote = document.querySelector('.quote')
let quoteNumber = document.querySelector('.quote-number')
let quotesData = []
let counter = 0

nextButton.addEventListener('click', clickHandler)

fetch("https://type.fit/api/quotes")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        quotesData = data
        console.log(data[0])
        console.log(quotesData)
        author.innerText = quotesData[counter].author
        quote.innerText = quotesData[counter].text ? quotesData[counter].text : 'N/A'
        quoteNumber.innerText = counter + 1
    });

function clickHandler(e) {
    containerDiv.style.animation = 'animation 500ms linear'
    setTimeout(() => {
        counter++
        author.innerText = quotesData[counter].author
        quote.innerText = quotesData[counter].text ? quotesData[counter].text : 'N/A'
        quoteNumber.innerText = counter + 1
        containerDiv.style.animation = 'loading 200ms linear forwards'
    }, 400)
}