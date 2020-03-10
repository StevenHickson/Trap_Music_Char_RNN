require 'nn'

local PinningActivationOne = torch.class('nn.PinningActivationOne', 'nn.Module')

function PinningActivationOne:updateOutput(input)

  -- TODO ---------------------------
  self.output:resizeAs(input):fill(1)

  -----------------------------------

  return self.output
end

function PinningActivationOne:updateGradInput(input, gradOutput)

  -- TODO ---------------------------
  self.gradInput:resizeAs(input):fill(0)
  --self.gradInput:cmul(gradOutput)
  --self.gradInput = gradOutput
  -----------------------------------

  return self.gradInput
end

