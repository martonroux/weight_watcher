<template>
  <button :class="{'btn': !btnClicked, 'btn-active': btnClicked}" @click="handleClick">
    {{ text }}
  </button>
</template>

<script>
export default {
  data () {
    return {
      btnClicked: false,
    }
  },
  props: ['text'],
  methods: {
    handleClick() {
      this.btnClicked = true;

      setTimeout(() => {
        this.btnClicked = false;
        this.$emit('clicked');
      }, 200);
    }
  }
}
</script>

<style scoped>

.btn:hover {
  scale: 96%;
}

.btn-active {
  scale: 90%;
}

</style>