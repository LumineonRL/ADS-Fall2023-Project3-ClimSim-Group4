import platform
import psutil
import GPUtil

class SystemInfo:
    def get_cpu_info(self) -> str:
        cpu_info = platform.processor()
        return f"CPU: {cpu_info}"

    def get_cpu_cores(self) -> int:
        cpu_count = psutil.cpu_count(logical=False)
        return cpu_count

    def get_cpu_frequency(self) -> float:
        cpu_freq = psutil.cpu_freq().current
        return cpu_freq

    def get_ram_info(self) -> float:
        ram_info = psutil.virtual_memory()
        ram_total_gb = ram_info.total / (1024**3)
        return ram_total_gb

    def get_virtual_memory_info(self) -> float:
        vm_info = psutil.swap_memory()
        vm_total_gb = vm_info.total / (1024**3)
        return vm_total_gb

    def get_gpu_info(self) -> list:
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_total_gb = gpu.memoryTotal / 1024
            gpu_info.append({"name": gpu.name, "memory": gpu_total_gb})
        return gpu_info