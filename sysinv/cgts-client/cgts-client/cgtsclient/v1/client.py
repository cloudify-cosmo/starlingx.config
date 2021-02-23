# Copyright 2012-2020 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Copyright (c) 2013-2021 Wind River Systems, Inc.
#


from ..common import http
from ..v1 import address
from ..v1 import address_pool
from ..v1 import app
from ..v1 import ceph_mon
from ..v1 import certificate
from ..v1 import cluster
from ..v1 import controller_fs
from ..v1 import datanetwork
from ..v1 import device_image
from ..v1 import device_image_state
from ..v1 import device_label
from ..v1 import drbdconfig
from ..v1 import ethernetport
from ..v1 import fernet
from ..v1 import health
from ..v1 import helm
from ..v1 import host_fs
from ..v1 import icpu
from ..v1 import idisk
from ..v1 import idns
from ..v1 import iextoam
from ..v1 import ihost
from ..v1 import iinterface
from ..v1 import ilvg
from ..v1 import imemory
from ..v1 import inode
from ..v1 import interface_datanetwork
from ..v1 import interface_network
from ..v1 import intp
from ..v1 import iprofile
from ..v1 import ipv
from ..v1 import isensor
from ..v1 import isensorgroup
from ..v1 import istor
from ..v1 import isystem
from ..v1 import iuser
from ..v1 import kube_cluster
from ..v1 import kube_host_upgrade
from ..v1 import kube_upgrade
from ..v1 import kube_version
from ..v1 import label
from ..v1 import license
from ..v1 import lldp_agent
from ..v1 import lldp_neighbour
from ..v1 import load
from ..v1 import network
from ..v1 import partition
from ..v1 import pci_device
from ..v1 import port
from ..v1 import ptp
from ..v1 import registry_image
from ..v1 import remotelogging
from ..v1 import restore
from ..v1 import route
from ..v1 import sdn_controller
from ..v1 import service_parameter
from ..v1 import sm_service
from ..v1 import sm_service_nodes
from ..v1 import sm_servicegroup
from ..v1 import storage_backend
from ..v1 import storage_ceph
from ..v1 import storage_ceph_external
from ..v1 import storage_ceph_rook
from ..v1 import storage_external
from ..v1 import storage_file
from ..v1 import storage_lvm
from ..v1 import storage_tier
from ..v1 import upgrade


class Client(http.HTTPClient):
    """Client for the Cgts v1 API.

    :param string endpoint: A user-supplied endpoint URL for the cgts
                            service.
    :param function token: Provides token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the Cgts v1 API."""
        super(Client, self).__init__(*args, **kwargs)
        self.smapi_endpoint = kwargs.get('smapi_endpoint')

        self.isystem = isystem.isystemManager(self)
        self.ihost = ihost.ihostManager(self)
        self.inode = inode.inodeManager(self)
        self.icpu = icpu.icpuManager(self)
        self.imemory = imemory.imemoryManager(self)
        self.iinterface = iinterface.iinterfaceManager(self)
        self.idisk = idisk.idiskManager(self)
        self.istor = istor.istorManager(self)
        self.ipv = ipv.ipvManager(self)
        self.ilvg = ilvg.ilvgManager(self)
        self.iuser = iuser.iuserManager(self)
        self.idns = idns.idnsManager(self)
        self.intp = intp.intpManager(self)
        self.ptp = ptp.ptpManager(self)
        self.iextoam = iextoam.iextoamManager(self)
        self.controller_fs = controller_fs.ControllerFsManager(self)
        self.storage_backend = storage_backend.StorageBackendManager(self)
        self.storage_lvm = storage_lvm.StorageLvmManager(self)
        self.storage_file = storage_file.StorageFileManager(self)
        self.storage_external = storage_external.StorageExternalManager(self)
        self.storage_ceph = storage_ceph.StorageCephManager(self)
        self.storage_ceph_rook = storage_ceph_rook.StorageCephRookManager(self)
        self.ceph_mon = ceph_mon.CephMonManager(self)
        self.drbdconfig = drbdconfig.drbdconfigManager(self)
        self.iprofile = iprofile.iprofileManager(self)
        self.port = port.PortManager(self)
        self.ethernet_port = ethernetport.EthernetPortManager(self)
        self.address = address.AddressManager(self)
        self.address_pool = address_pool.AddressPoolManager(self)
        self.route = route.RouteManager(self)
        self.isensor = isensor.isensorManager(self)
        self.isensorgroup = isensorgroup.isensorgroupManager(self)
        self.pci_device = pci_device.PciDeviceManager(self)
        self.load = load.LoadManager(self)
        self.upgrade = upgrade.UpgradeManager(self)
        self.network = network.NetworkManager(self)
        self.datanetwork = datanetwork.DataNetworkManager(self)
        self.interface_datanetwork = \
            interface_datanetwork.InterfaceDataNetworkManager(self)
        self.interface_network = interface_network.InterfaceNetworkManager(self)
        self.service_parameter = service_parameter.ServiceParameterManager(self)
        self.cluster = cluster.ClusterManager(self)
        self.lldp_agent = lldp_agent.LldpAgentManager(self)
        self.lldp_neighbour = lldp_neighbour.LldpNeighbourManager(self)
        self.sm_service_nodes = sm_service_nodes.SmNodesManager(self)
        self.sm_service = sm_service.SmServiceManager(self)
        self.sm_servicegroup = sm_servicegroup.SmServiceGroupManager(self)
        self.health = health.HealthManager(self)
        self.registry_image = registry_image.RegistryImageManager(self)
        self.remotelogging = remotelogging.RemoteLoggingManager(self)
        self.sdn_controller = sdn_controller.SDNControllerManager(self)
        self.partition = partition.partitionManager(self)
        self.license = license.LicenseManager(self)
        self.certificate = certificate.CertificateManager(self)
        self.storage_tier = storage_tier.StorageTierManager(self)
        self.storage_ceph_external = \
            storage_ceph_external.StorageCephExternalManager(self)
        self.helm = helm.HelmManager(self)
        self.label = label.KubernetesLabelManager(self)
        self.fernet = fernet.FernetManager(self)
        self.app = app.AppManager(self)
        self.host_fs = host_fs.HostFsManager(self)
        self.kube_cluster = kube_cluster.KubeClusterManager(self)
        self.kube_version = kube_version.KubeVersionManager(self)
        self.kube_upgrade = kube_upgrade.KubeUpgradeManager(self)
        self.kube_host_upgrade = kube_host_upgrade.KubeHostUpgradeManager(self)
        self.device_image = device_image.DeviceImageManager(self)
        self.device_image_state = device_image_state.DeviceImageStateManager(self)
        self.device_label = device_label.DeviceLabelManager(self)
        self.restore = restore.RestoreManager(self)
