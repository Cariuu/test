function iniciar(){
    edad=document.getElementById("miedad");
    edad.addEventListener("change", cambiarrango, false);
    document.informacion.addEventListener("invalid", validacion, true);
    document.getElementById("enviar").addEventListener("click", enviar, false);
}
function cambiarrango(){
    var salida=document.getElementById("rango");
    var calc=edad.value-20;
    if(calc<20){
        calc=0;
        edad.value=20;
    } 
    salida.innerHTML=calc+ "a" +edad.value;
}
function validacion (e){
    var elemento=e.target;
    elemento.style.background=`#FFDDDD`;
}
function enviar (){
    var valido=document.informacion.checkValidity();
    if(valido){
        document.informacion.submit();
    }
}
window.addEventListener("load", iniciar, false);
