<script setup>
</script>

<template>
  <div class="menu-dropdown">
    <ul>
      <li v-for="(redir, index) in listRedirects" :key="index">
        <h1 class="menu-options" @click="onClick(redir.id)">
          {{ redir.name }}
        </h1>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      listRedirects: [
        {
          id: 0, name: "Home", link: "/"
        },
        {
          id: 1, name: "Stats", link: "/stats"
        },
        {
          id: 2, name: "Workouts", link: "/workouts"
        },
      ]
    }
  },
  methods: {
    onClick(id) {
      const element = this.listRedirects.find(item => item.id === id);

      element.isClicked = true;

      if (element) {
        this.$router.push(element.link);
      } else {
        console.log("Error while searching for elem with ID in listRedirects");
      }
      setTimeout(() => {
        this.$emit('clicked', true);
      }, 100);
    }
  }
}
</script>

<style scoped>

.menu-dropdown {
  height: 0;
  color: var(--text-white);
  background: white;
  transition: color 0.1s;
}

.menu-dropdown h1 {
  margin-bottom: 6vw;
}

.menu-options {
  cursor: pointer;
  transition: scale 0.2s;
}

.menu-options:hover {
  scale: 96%;
}

.menu-options:active {
  scale: 90%;
}

</style>