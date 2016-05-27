hide_page=false;
django.jQuery(document).ready(function(){
	//jQuery("checkbox:fist")
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
    
    if(django.jQuery("select:last")) {
    	django.jQuery(".field-diapago").hide();
    	django.jQuery(".field-meses").hide();
        //django.jQuery(".field-total").hide();
    }
    
    django.jQuery('#id_tipopago').change(function() {
        if (django.jQuery(this).find(':selected').val() === 'CONTADO') {
        	//alert('entra al if')
        	django.jQuery(".field-diapago").slideUp('slow');
        	django.jQuery(".field-meses").slideUp('slow');
            //django.jQuery(".field-total").slideUp('slow');
        } else {
        	django.jQuery(".field-diapago").slideDown('slow');
        	django.jQuery(".field-meses").slideDown('slow');
            //django.jQuery(".field-total").slideDown('slow');
        }
    });
    
})