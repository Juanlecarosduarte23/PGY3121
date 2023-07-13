

        $(document).ready(function(){

    $("#revisar").click(function(){
        $.get("https://mindicador.cl/api/dolar/20-06-2023",function(data){

            $.each(data.serie,function(i,item)
            {
                $("#dolar").append("<tr><td>" + item.fecha + "</td><td>"+ item.valor );

            });

        })

    });
});

