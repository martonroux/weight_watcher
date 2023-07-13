<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div v-if="open" class="popup-window">
    <div class="popup-content">
      <slot></slot>
    </div>
    <div class="row-div">
      <Button :text="'OK'" @clicked="closePopup(true)"/>
      <Button :text="'Cancel'" @clicked="closePopup(false)"/>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    open: {
      type: Boolean,
      required: true
    }
  },
  emits: ['closed'],
  methods: {
    closePopup(isOk) {
      this.$emit('closed', isOk);
    }
  }
};
</script>

<style scoped>
.popup-window {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;

  :not(:last-child) {
    margin-right: 10px;
  }
}

.row-div {
  display: flex;
  flex-direction: row;
}

.popup-content {
  background-color: var(--widget-color);
  padding: 20px;
  border-radius: var(--widget-border-radius);
}

@media (max-width: 600px) {
  .popup-window {
    flex-direction: column;

    :not(:last-child) {
      margin-right: 0;
    }
  }

  .row-div {
    margin-top: 10px;

    :not(:last-child) {
      margin-right: 10px;
    }
  }
}

@media (max-width: 350px) {
  .popup-content {
    width: 80vw;
  }
}

</style>