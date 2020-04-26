<template>
    <div class="description">
        <p>
            {{ text }}
        </p>
    </div>
</template>

<script>
export default {
    props: ['text'],
    name: 'Description'
}
</script>
