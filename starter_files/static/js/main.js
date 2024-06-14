let generate_btn = document.getElementById("generate_btn");
let save_btn = document.getElementsByTagName("button");

function processing(){
    generate_btn.value = "wait while processing...";
}

function saving(myvar){    
    for(i=0 ; i<save_btn.length ; i++){ 
        if (save_btn[i].value == myvar){
            save_btn[i].innerHTML = "wait while saving...";
        }
    }       
}
