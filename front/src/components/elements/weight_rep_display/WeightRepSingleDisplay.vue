<template>
  <div class="widget">
    <ol class="flex-container">
      <li class="list" v-for="(rep, index) in repsList" :key="index">
        <div class="list-content" :class="{'list-content-active': index > 0}">
          <p :class="{'tilt-shaking-anim': editActive}">{{ rep }} rep</p>
          <p :class="{'tilt-shaking-anim': editActive}">{{ weightList[index] }} kg</p>
        </div>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  props: ['repsList', 'weightList', 'editActive']
}
</script>

<style scoped>

.widget {
  background-color: var(--backround-color);
  border: 2px solid var(--text-white);
  border-radius: var(--widget-border-radius);
  display: flex;
  justify-content: flex-start;
  padding: 12px;
}

.widget p {
  color: var(--text-transparent);
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
}

.list {
  flex: 0 0 auto;
}

.list-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.list-content-active {
  margin-left: 20px;
}

</style>