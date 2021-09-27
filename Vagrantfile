Vagrant.configure("2") do |config|
    config.vm.box = "mazenovi/linuxmint"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end