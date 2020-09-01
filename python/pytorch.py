import torch

x = torch.randn(10000, 10000).to("cuda")
w = torch.randn(10000, 10000).to("cuda")
# ensure that context initialization finish before you start measuring time
torch.cuda.synchronize()

y = x.mm(w.t())
