<template>
  <img :class="{'wrkt-image': !imgClicked, 'wrkt-image-active': imgClicked}"
        :src="imgPath" alt="edit" @click="wrktImageClicked">
</template>

<script>
export default {
  data () {
    return {
      imgPath: "./src/assets/icons/edit.png",
      imgClicked: false,
      isEditing: false,
    }
  },
  methods: {
    wrktImageClicked() {
      this.imgClicked = true;
      this.isEditing = !this.isEditing;

      if (this.isEditing === false) {
        this.imgPath = "./src/assets/icons/edit.png";
      } else {
        this.imgPath = "./src/assets/icons/check.png";
      }
      setTimeout(() => {
        this.imgClicked = false;
        this.$emit('clicked');
      }, 200);
    }
  }
}
</script>

<style scoped>

.wrkt-image {
  transition: scale 0.2s;
  cursor: pointer;
}

.wrkt-image:hover {
  scale: 96%;
}

.wrkt-image-active {
  scale: 90%;
}

</style>