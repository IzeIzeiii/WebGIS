<template>
  <div>
    <el-select v-model="value" placeholder="请选择">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      >
      </el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      options: [
        {
          value: "选项1",
          label: "日用品",
        },
        {
          value: "选项2",
          label: "生鲜",
        },
        {
          value: "选项3",
          label: "食品",
        },
        {
          value: "选项4",
          label: "电子产品",
        },
        {
          value: "选项5",
          label: "钝角",
        },
      ],
      value: "",
    };
  },
};
</script>

<style>
</style>