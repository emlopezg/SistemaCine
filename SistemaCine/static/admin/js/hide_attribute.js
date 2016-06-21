hide_page=false;
django.jQuery(document).ready(function(){
	//*****RESERVA DE ASIENTO FUNCTIONS*****//
	if (django.jQuery("#id_pagado").prop('checked')) {
		django.jQuery("#id_fechareserva").prop('disabled', true);
		django.jQuery("#id_usuario").prop('disabled', true);
		django.jQuery("#id_proyeccion").prop('disabled', true);
		django.jQuery("#id_horario").prop('disabled', true);
		django.jQuery("#id_cantidad_menor").prop('disabled', true);
		django.jQuery("#id_cantidad_mayor").prop('disabled', true);
		django.jQuery("#id_asientos").prop('disabled', true);
		django.jQuery("#id_fechafuncion").prop('disabled', true);
		django.jQuery("#id_totalentrada").prop('disabled', true);
		django.jQuery("#id_combo").prop('disabled', true);
		django.jQuery("#id_totalcombo").prop('disabled', true);
		django.jQuery("#id_total").prop('disabled', true);
		django.jQuery("#id_pagado").prop('disabled', true);
		
		//var texto = 'Pelicula: ',;
		//jAlert(, 'Alert Dialog');
		//$('#popup').fadeIn('slow');
        //$('.popup-overlay').fadeIn('slow');
        //alert()
        //$('.popup-overlay').height($(window).height());
	}
	
	
	//*****ORDEN DE COMPRA FUNCTIONS*****//
	
	//estos campos deben estar vacios cada vez que hay una nueva recepcion
	django.jQuery("#id_fecharecepcion").val("");
	django.jQuery("#id_fechaemision").val("");
	django.jQuery("#id_cantidadrecibida").val("");
	django.jQuery("#id_factura").val("");
	django.jQuery("#id_dia").val("");
	
	//cuando una orden de compra se anula, se deshabilitan los campos de esa orden
	if (django.jQuery("#id_estado").prop('checked')) {
		//alert('entra')
		django.jQuery("#id_fecha").prop('disabled', true);
		django.jQuery("#id_producto").prop('disabled', true);
		django.jQuery("#id_proveedor").prop('disabled', true);
		django.jQuery("#id_cantidad_producto").prop('disabled', true);
		django.jQuery("#id_medida").prop('disabled', true);
		django.jQuery("#id_total").prop('disabled', true);
		django.jQuery("#id_aprobado").prop('disabled', true);
		django.jQuery("#id_cantidadrecibida").prop('disabled', true);
		django.jQuery("#id_fecharecepcion").prop('disabled', true);
		django.jQuery("#id_fechaemision").prop('disabled', true);
		django.jQuery("#id_factura").prop('disabled', true);
		django.jQuery("#id_tipopago").prop('disabled', true);
		django.jQuery("#id_estado").prop('disabled', true);
    }
	
	//fields dependientes del tipo de pago
	if(django.jQuery("select:last")) {
    	django.jQuery(".field-diapago").hide();
    	django.jQuery(".field-meses").hide();
        //django.jQuery(".field-total").hide();
    }
    
    
    django.jQuery('#id_tipopago').change(function() {
        if (django.jQuery(this).find(':selected').val() === 'AMORTIZADO') {
        	//alert('entra al if')
        	django.jQuery(".field-diapago").slideDown('slow');
        	django.jQuery(".field-meses").slideDown('slow');
            //django.jQuery(".field-total").slideDown('slow');
        } else {
        	django.jQuery(".field-diapago").slideUp('slow');
        	django.jQuery(".field-meses").slideUp('slow');
            //django.jQuery(".field-total").slideUp('slow');
        }
    });
    
  //para que siga mostrando aunque no se haya usado el select
	if(django.jQuery("#id_tipopago").find(':selected').val() === 'AMORTIZADO'){
    	django.jQuery(".field-diapago").slideDown('slow');
    	django.jQuery(".field-meses").slideDown('slow');
    }else{
    	django.jQuery(".field-diapago").slideUp('slow');
		django.jQuery(".field-meses").slideUp('slow');
	}
    

    /**if (django.jQuery("checkbox:last").not(":checked")) {
    	//alert("hola")
    	//alert(django.jQuery(".form-row field-fechafactura"))
    	django.jQuery(".field-fecharecepcion").hide();
    	django.jQuery(".field-fechaemision").hide();
        django.jQuery(".field-factura").hide();
        hide_page=true;
    }else{
    	//alert("entra al else")
    	//django.jQuery(".field-fecharecepcion").show();
    	//django.jQuery(".field-fechaemision").show();
        //django.jQuery(".field-factura").show();
        hide_page=false;
    }
    
    django.jQuery("#id_estado").click(function(){
        hide_page=!hide_page;
        if(hide_page)
        {
        	django.jQuery(".field-fecharecepcion").slideUp('slow');
        	django.jQuery(".field-fechaemision").slideUp('slow');
        	django.jQuery(".field-factura").slideUp('slow');
        }else
        {
        	django.jQuery(".field-fecharecepcion").slideDown('slow');
        	django.jQuery(".field-fechaemision").slideDown('slow');
            django.jQuery(".field-factura").slideDown('slow');
        }
    })**/
    
    
})