<script setup>
import DropdownMenu from "@/components/DropdownMenu.vue";
</script>

<template>
  <div class="banner" :class="{ 'banner_active': dropDownVisible }">
    <img src="../assets/icons/logo.png" alt="logo" class="logo">
    <div class="menu-btn" id="menu-btn">
      <div>
        <span class="line-1"></span>
        <span class="line-2"></span>
        <span class="line-3"></span>
      </div>
    </div>
    <div class="dropdown-container" v-show="dropDownVisible">
      <DropdownMenu :drop-down-visible="dropDownVisible" @clicked="handleDropDrownClicked"></DropdownMenu>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dropDownVisible: false,
    };
  },
  mounted() {
    let menu = document.getElementById("menu-btn");

    menu.onclick = () => {
      menu.classList.toggle("openmenu");
      this.toggleDropDown();
    }
  },
  methods: {
    toggleDropDown() {
      this.dropDownVisible = !this.dropDownVisible;
    },
    handleDropDrownClicked() {
      let menu = document.getElementById("menu-btn");

      this.dropDownVisible = false;
      menu.classList.toggle("openmenu");
    }
  }
};
</script>

<style scoped>
.banner {
  display: flex;
  justify-content: flex-end;
  background-color: var(--banner-color);
  align-items: flex-start;
  padding: 20px 40px 20px 20px;
  height: 80px;
  transition: height 0.5s;
}

.logo {
  width: 50px;
  height: auto;
  padding: 20px;
  margin-right: auto;
}

.dropdown-container {
  position: absolute;
  left: 20px;
  top: 90px;
}

.banner_active {
  height: var(--drop-down-size);
}

.menu-btn {
  width: 80px;
  height: 80px;
  cursor: pointer;
}

.menu-btn div {
  width: 60%;
  height: 60%;
  position: relative;
  top: 18%;
  left: 20%;
}

.menu-btn span {
  background: var(--text-white);
  width: 100%;
  height: 6px;
  border-radius: 5px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: transform 0.5s, width 0.5s;
}

.menu-btn .line-1 {
  transform: translate(-50%, -300%);
}

.menu-btn .line-3 {
  transform: translate(-50%, 200%);
}

.openmenu .line-1 {
  transform: translate(-50%, -50%) rotate(-45deg);
}

.openmenu .line-3 {
  transform: translate(-50%, -50%) rotate(45deg);
}

.openmenu .line-2 {
  width: 0;
}

</style>