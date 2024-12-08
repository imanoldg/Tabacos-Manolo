document.addEventListener("keyup", e=>{

    if(e.target.matches(".buscador")){

        document.querySelectorAll("#marca").forEach(marca =>{

            if(marca.textContent.toLowerCase().includes(e.target.value.toLowerCase())){
                marca.classList.remove("filtro")
            } else{
                marca.classList.add("filtro")
            }
            
        })

        document.querySelectorAll("#cliente_miniInfo").forEach(cliente =>{

            if(cliente.textContent.toLowerCase().includes(e.target.value.toLowerCase())){
                cliente.classList.remove("filtro")
            } else{
                cliente.classList.add("filtro")
            }
            
        })


        document.querySelectorAll(".paquete").forEach(paquete =>{

            if(paquete.textContent.toLowerCase().includes(e.target.value.toLowerCase())){
                paquete.classList.remove("filtro")
            } else{
                paquete.classList.add("filtro")
            }
            
        })


    }


})