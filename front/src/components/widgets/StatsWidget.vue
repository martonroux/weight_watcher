<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="widget">
    <h2 style="color: var(--accentuation-color); margin-bottom: 2vh">
      STATS {{ additionalText }}
    </h2>
    <div class="evol">
      <div class="evol-text">
        <h2>One month</h2>
        <h2>evolution</h2>
      </div>
      <div class="evol-value">
        <h2>{{ growthPercent >= 0 ? '+' : '' }}{{ growthPercent }}%</h2>
      </div>
    </div>
    <Button :text="'All stats'" style="margin-top: 4vw" @clicked="clickedAllStats"/>
  </div>
</template>

<script>
export default {
  data () {
    return {
      allStatsUrl: "/stats",
    }
  },
  props: ['growthPercent', 'additionalText'],
  methods: {
    clickedAllStats() {
      this.$router.push(this.allStatsUrl);
    }
  }
}
</script>

<style scoped>

.widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
}

.evol {
  display: flex;
  flex-direction: row;
}

.evol .evol-value {
  margin-left: auto;
}

.evol .evol-text {
  margin-right: auto;
}

.evol-value {
  background-image: linear-gradient(to bottom right, var(--accentuation-color), transparent);
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

</style>