<template>
  <button :class="{'btn': !allStatsClicked, 'btn-active': allStatsClicked}" @click="handleClick">
    {{ text }}
  </button>
</template>

<script>
export default {
  data () {
    return {
      allStatsClicked: false,
    }
  },
  props: ['url', 'text'],
  methods: {
    handleClick() {
      this.allStatsClicked = true;

      setTimeout(() => {
        this.allStatsClicked = false;
        this.$router.push(this.url);
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