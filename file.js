import data from './file.json'assert{type:'json'};

data.sort((a,b)=>b-a);

let i=0;
let sum=0;
while (i<3){
    sum=sum+data[i];
    console.log(sum);
    i++
    
}
console.log('sum : '+sum);
