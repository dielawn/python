let "groceries" = {
    Produce: {
        onion: 1;
        bell-pepper: 1
        apples: 5
        },
    Dairy: {
        honey-yogurt: 1
        sour-cream: 1
        }
    
    }


function getArrayOfGroseries(obj){
    return Object.keys(obj)
console.log(getArrayOfGroceries(groceries));
