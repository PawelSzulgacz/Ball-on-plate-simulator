document.getElementById('inputfile').addEventListener('change', function() {
var obrazek= document.getElementById("kanwa");
var ctx = obrazek.getContext("2d")
var x=600;
var y=500;

var file=new FileReader();

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

file.onload=async function(){

    let = file.result;
    let = let.split(" ");
    var help1 = 0;
    var help2 = 0;
    var tablica = new Float32Array(100);
    //document.getElementById("output").innerHTML = let[353]

    ctx.strokeStyle ="rgb(0, 0, 0)"
    for(var i = 0;i<99;i++)
    {
    ctx.fillStyle = 'rgb(191, 145, 5)';
    ctx.fillRect(0, 0, x, y);
    ctx.arc(let[0+i*4]*2500, let[1+i*4]*2500, 20, 0, 2 * Math.PI);
    ctx.fillStyle = 'rgb(128, 128, 128)';
    ctx.fill();
    ctx.fillStyle = 'rgb(0, 0, 0)';
    ctx.fillRect(500,0,100,500);//czarny
    ctx.fillStyle = 'rgb(256, 256, 256)';
    ctx.fillRect(525,25,50,200);
    ctx.fillRect(525,275,50,200);//biale
    ctx.fillStyle = 'rgb(256, 0, 0)';
    if(let[2+i*4] > 0)
    {
    ctx.fillRect(535,125-let[2+i*4]*20,30,let[2+i*4]*20);//czerwone
    }
    else
    {
    ctx.fillRect(535,125,30,Math.abs(let[2+i*4]*20));
    }
    if(let[3+i*4] > 0)
    {
    ctx.fillRect(535,375-let[3+i*4]*20,30,let[3+i*4]*20);
    }
    else
    {
    ctx.fillRect(535,375,30,Math.abs(let[3+i*4]*20));
    }
    ctx.stroke();
    ctx.beginPath();
    await sleep(100);

    }
    
}
  
file.readAsText(this.files[0]);
})