function redirectDate(){
    const input = document.querySelector('#dataDate').value;
    location.replace('/graphs?date=' + input)
}