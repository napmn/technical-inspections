<template>
    <div class="description">
        <p>
            {{ text }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'Description',
    props: ['text'],
}
</script>
