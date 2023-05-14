<template>
    <div class="is-danger">
        <h1 class="title">An error has occurred</h1>
        <p>
            {{ error }}
        </p>
    </div>

</template>

<script>

 export default {
     name: "ErrorView",

     props: ["error"],
 }

</script>
