<template>
    <div class="description">
        <p v-html="text">
        </p>
    </div>
</template>

<script>
export default {
    name: 'Description',
    props: ['text'],
}
</script>
