# Copyright 2017 Brocade Communications Systems, Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Link Type Constants

See:  http://www.tcpdump.org/linktypes.html
"""


LINKTYPE_NULL                             =   0
LINKTYPE_ETHERNET                         =   1
LINKTYPE_AX25                             =   3
LINKTYPE_IEEE802_5                        =   6
LINKTYPE_ARCNET_BSD                       =   7
LINKTYPE_SLIP                             =   8
LINKTYPE_PPP                              =   9
LINKTYPE_FDDI                             =  10
LINKTYPE_PPP_HDLC                         =  50
LINKTYPE_PPP_ETHER                        =  51
LINKTYPE_ATM_RFC1483                      = 100
LINKTYPE_RAW                              = 101
LINKTYPE_C_HDLC                           = 104
LINKTYPE_IEEE802_11                       = 105
LINKTYPE_FRELAY                           = 107
LINKTYPE_LOOP                             = 108
LINKTYPE_LINUX_SLL                        = 113
LINKTYPE_LTALK                            = 114
LINKTYPE_PFLOG                            = 117
LINKTYPE_IEEE802_11_PRISM                 = 119
LINKTYPE_IP_OVER_FC                       = 122
LINKTYPE_SUNATM                           = 123
LINKTYPE_IEEE802_11_RADIOTAP              = 127
LINKTYPE_ARCNET_LINUX                     = 129
LINKTYPE_APPLE_IP_OVER_IEEE1394           = 138
LINKTYPE_MTP2_WITH_PHDR                   = 139
LINKTYPE_MTP2                             = 140
LINKTYPE_MTP3                             = 141
LINKTYPE_SCCP                             = 142
LINKTYPE_DOCSIS                           = 143
LINKTYPE_LINUX_IRDA                       = 144

LINKTYPE_USER0                            = 147
LINKTYPE_USER1                            = 148
LINKTYPE_USER2                            = 149
LINKTYPE_USER3                            = 150
LINKTYPE_USER4                            = 151
LINKTYPE_USER5                            = 152
LINKTYPE_USER6                            = 153
LINKTYPE_USER7                            = 154
LINKTYPE_USER8                            = 155
LINKTYPE_USER9                            = 156
LINKTYPE_USER10                           = 157
LINKTYPE_USER11                           = 158
LINKTYPE_USER12                           = 159
LINKTYPE_USER13                           = 160
LINKTYPE_USER14                           = 161
LINKTYPE_USER15                           = 162

LINKTYPE_IEEE802_11_AVS                   = 163
LINKTYPE_BACNET_MS_TP                     = 165
LINKTYPE_PPP_PPPD                         = 166
LINKTYPE_GPRS_LLC                         = 169
LINKTYPE_GPF_T                            = 170
LINKTYPE_GPF_F                            = 171
LINKTYPE_LINUX_LAPD                       = 177
LINKTYPE_BLUETOOTH_HCI_H4                 = 187
LINKTYPE_USB_LINUX                        = 189
LINKTYPE_PPI                              = 192
LINKTYPE_IEEE802_15_4                     = 195
LINKTYPE_SITA                             = 196
LINKTYPE_ERF                              = 197
LINKTYPE_BLUETOOTH_HCI_H4_WITH_PHDR       = 201
LINKTYPE_AX25_KISS                        = 202
LINKTYPE_LAPD                             = 203
LINKTYPE_PPP_WITH_DIR                     = 204
LINKTYPE_C_HDLC_WITH_DIR                  = 205
LINKTYPE_FRELAY_WITH_DIR                  = 206
LINKTYPE_IPMB_LINUX                       = 209
LINKTYPE_IEEE802_15_4_NONASK_PHY          = 215
LINKTYPE_USB_LINUX_MMAPPED                = 220
LINKTYPE_FC_2                             = 224
LINKTYPE_FC_2_WITH_FRAME_DELIMS           = 225
LINKTYPE_IPNET                            = 226
LINKTYPE_CAN_SOCKETCAN                    = 227
LINKTYPE_IPV4                             = 228
LINKTYPE_IPV6                             = 229
LINKTYPE_IEEE802_15_4_NOFCS               = 230
LINKTYPE_DBUS                             = 231
LINKTYPE_DVB_CI                           = 235
LINKTYPE_MUX27010                         = 236
LINKTYPE_STANAG_5066_D_PDU                = 237
LINKTYPE_NFLOG                            = 239
LINKTYPE_NETANALYZER                      = 240
LINKTYPE_NETANALYZER_TRANSPARENT          = 241
LINKTYPE_IPOIB                            = 242
LINKTYPE_MPEG_2_TS                        = 243
LINKTYPE_NG40                             = 244
LINKTYPE_NFC_LLCP                         = 245
LINKTYPE_INFINIBAND                       = 247
LINKTYPE_SCTP                             = 248
LINKTYPE_USBPCAP                          = 249
LINKTYPE_RTAC_SERIAL                      = 250
LINKTYPE_BLUETOOTH_LE_LL                  = 251
LINKTYPE_NETLINK                          = 253
LINKTYPE_BLUETOOTH_LINUX_MONITOR          = 254
LINKTYPE_BLUETOOTH_BREDR_BB               = 255
LINKTYPE_BLUETOOTH_LE_LL_WITH_PHDR        = 256
LINKTYPE_PROFIBUS_DL                      = 257
LINKTYPE_PKTAP                            = 258
LINKTYPE_EPON                             = 259
LINKTYPE_IPMI_HPM_2                       = 260
LINKTYPE_ZWAVE_R1_R2                      = 261
LINKTYPE_ZWAVE_R3                         = 262
LINKTYPE_WATTSTOPPER_DLM                  = 263
LINKTYPE_ISO_14443                        = 264
LINKTYPE_RDS                              = 265
LINKTYPE_USB_DARWIN                       = 266

#todo need test valid linktype
