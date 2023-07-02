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

      this.$emit('clicked');
      setTimeout(() => {
        this.btnClicked = false;
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