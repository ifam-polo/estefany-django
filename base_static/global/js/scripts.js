function my_scope(){
    const form = document.querySelectorAll('.form-delete');

    for(const form of forms){
        form.addEventListener('submit', function(e){
            e.preventDefault();

            const confirmed = confirm('Are your sure?')

            if (confirmed){
                form.submit();
            }
        });
    }
}

my_scope();