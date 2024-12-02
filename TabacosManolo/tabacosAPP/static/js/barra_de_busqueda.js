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

        document.querySelectorAll("#distribuidor").forEach(ds =>{

            console.log(ds.textContent)

            if(ds.textContent.toLowerCase().includes(e.target.value.toLowerCase())){
                ds.classList.remove("filtro")
            } else{
                ds.classList.add("filtro")
            }
            
        })

        document.querySelectorAll(".estanco").forEach(estanco =>{

            console.log(estanco.textContent)

            if(estanco.textContent.toLowerCase().includes(e.target.value.toLowerCase())){
                estanco.classList.remove("filtro")
            } else{
                estanco.classList.add("filtro")
            }
            
        })
    }


})